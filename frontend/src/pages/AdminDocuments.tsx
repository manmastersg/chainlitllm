import { useState } from 'react';
import { Navigate } from 'react-router-dom';

import Page from 'pages/Page';

import { useAuth } from '@chainlit/react-client';

import { Document, DocumentList } from '../components/admin/DocumentList';
import { DocumentUploader } from '../components/admin/DocumentUploader';

import { usePageIndex } from '../hooks/usePageIndex';

const AdminDocuments = () => {
  const { user } = useAuth();
  const role = user?.metadata?.role;
  const { documents, status, uploadDocument, deleteDocument, isLoading } =
    usePageIndex();
  const [uploading, setUploading] = useState(false);

  if (role !== 'admin') {
    return <Navigate to="/" replace />;
  }

  const handleUpload = async (file: File) => {
    setUploading(true);
    try {
      await uploadDocument(file);
    } finally {
      setUploading(false);
    }
  };

  const handleView = (doc: Document) => {
    // TODO: Open document structure modal
    alert(`View document ${doc.filename}`);
  };

  return (
    <Page>
      <div className="max-w-5xl mx-auto py-8 px-4">
        <h1 className="text-2xl font-bold mb-1">Document Management</h1>
        <p className="text-gray-500 mb-8">
          Upload and manage your knowledge base documents.
        </p>

        <DocumentUploader onUpload={handleUpload} disabled={uploading} />

        {status && (
          <div className="mt-6 p-3 bg-gray-50 rounded-lg text-sm text-gray-600">
            {status.total} documents | {status.ready} ready
            {status.total > status.ready &&
              ` | ${status.total - status.ready} indexing`}
          </div>
        )}

        {!isLoading && (
          <DocumentList
            documents={documents}
            onView={handleView}
            onDelete={deleteDocument}
          />
        )}
      </div>
    </Page>
  );
};

export default AdminDocuments;
