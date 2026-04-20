import { useCallback } from 'react';
import {
  DropzoneOptions,
  FileRejection,
  FileWithPath,
  useDropzone
} from 'react-dropzone';

import type { FileSpec } from 'client-types/';

interface useUploadProps {
  onError?: (error: string) => void;
  onResolved: (payloads: FileWithPath[]) => void;
  options?: DropzoneOptions;
  spec: FileSpec;
}

const useUpload = ({ onError, onResolved, options, spec }: useUploadProps) => {
  const onDrop: DropzoneOptions['onDrop'] = useCallback(
    (acceptedFiles: FileWithPath[], fileRejections: FileRejection[]) => {
      if (fileRejections.length > 0) {
        if (fileRejections[0].errors[0].code === 'file-too-large') {
          onError?.(`File is larger than ${spec.max_size_mb} MB`);
        } else {
          onError?.(fileRejections[0].errors[0].message);
        }
      }

      if (!acceptedFiles.length) return;
      return onResolved(acceptedFiles);
    },
    [spec]
  );

  let dzAccept: Record<string, string[]> = {};
  const accept = spec.accept;

  const isValidMimeType = (mimeType: string): boolean => {
    if (mimeType === '*/*') return false;
    const validWildcards = ['image/*', 'audio/*', 'video/*'];
    if (validWildcards.includes(mimeType)) return true;
    return true;
  };

  if (Array.isArray(accept)) {
    accept.forEach((a) => {
      if (typeof a === 'string' && isValidMimeType(a)) {
        dzAccept[a] = [];
      }
    });
  } else if (typeof accept === 'object') {
    Object.entries(accept).forEach(([key, value]) => {
      if (isValidMimeType(key)) {
        dzAccept[key] = value || [];
      }
    });
  }

  if (Object.keys(dzAccept).length === 0) {
    dzAccept = {
      'application/pdf': [],
      'image/*': [],
      'application/msword': [],
      'application/vnd.openxmlformats-officedocument.wordprocessingml.document':
        [],
      'application/vnd.ms-excel': [],
      'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet': [],
      'application/vnd.ms-powerpoint': [],
      'application/vnd.openxmlformats-officedocument.presentationml.presentation':
        []
    };
  }

  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    onDrop,
    maxFiles: spec.max_files || undefined,
    accept: dzAccept,
    maxSize: (spec.max_size_mb || 2) * 1000000,
    ...options
  });

  return { getInputProps, getRootProps, isDragActive };
};

export { useUpload };
