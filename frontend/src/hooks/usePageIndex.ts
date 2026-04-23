import { useCallback, useEffect } from "react";
import { useApi } from "@chainlit/react-client";
import { Document } from "../components/admin/DocumentList";

export const usePageIndex = () => {
  const { data: documents, mutate, error } = useApi<Document[]>(
    "/project/pageindex/documents",
    { refreshInterval: 2000 }
  );

  const { data: status } = useApi<{ total: number; ready: number; ready_doc_ids: string[] }>(
    "/project/pageindex/documents/status",
    { refreshInterval: 2000 }
  );

  const uploadDocument = useCallback(
    async (file: File) => {
      const formData = new FormData();
      formData.append("file", file);

      const res = await fetch("/chats/project/pageindex/documents", {
        method: "POST",
        body: formData,
      });

      await mutate();
      return res.json();
    },
    [mutate]
  );

  const deleteDocument = useCallback(
    async (doc: Document) => {
      await fetch(`/chats/project/pageindex/documents/${doc.doc_id}`, {
        method: "DELETE",
      });
      await mutate();
    },
    [mutate]
  );

  useEffect(() => {
    const handleProgress = (e: CustomEvent) => {
      const data = e.detail;
      
      // Force an immediate re-fetch of the documents list to get the updated progress
      // Alternatively we could optimistically update the cache here
      mutate();
      
      console.log("PageIndex progress", data);
    };

    window.addEventListener("pageindex_progress", handleProgress as EventListener);
    return () => window.removeEventListener("pageindex_progress", handleProgress as EventListener);
  }, [mutate]);

  return {
    documents: documents || [],
    status,
    isLoading: !documents && !error,
    uploadDocument,
    deleteDocument,
    refresh: mutate,
  };
};