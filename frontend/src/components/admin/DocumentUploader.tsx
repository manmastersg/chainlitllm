import { Upload } from 'lucide-react';
import { useCallback, useState } from 'react';

interface DocumentUploaderProps {
  onUpload: (file: File) => Promise<void>;
  disabled?: boolean;
}

export const DocumentUploader = ({
  onUpload,
  disabled
}: DocumentUploaderProps) => {
  const [isDragging, setIsDragging] = useState(false);

  const handleDrop = useCallback(
    async (e: React.DragEvent) => {
      e.preventDefault();
      setIsDragging(false);
      if (disabled) return;

      const files = Array.from(e.dataTransfer.files);
      for (const file of files) {
        if (file.type === 'application/pdf') {
          await onUpload(file);
        }
      }
    },
    [onUpload, disabled]
  );

  const handleFileInput = useCallback(
    async (e: React.ChangeEvent<HTMLInputElement>) => {
      if (disabled || !e.target.files) return;
      for (const file of Array.from(e.target.files)) {
        await onUpload(file);
      }
      e.target.value = '';
    },
    [onUpload, disabled]
  );

  return (
    <div
      onDragOver={(e) => {
        e.preventDefault();
        if (!disabled) setIsDragging(true);
      }}
      onDragLeave={() => setIsDragging(false)}
      onDrop={handleDrop}
      className={`
        border-2 border-dashed rounded-xl p-8 text-center transition-all cursor-pointer
        ${isDragging ? 'border-blue-500 bg-blue-50' : 'border-gray-300 hover:border-gray-400'}
        ${disabled ? 'opacity-50 cursor-not-allowed' : ''}
      `}
    >
      <input
        type="file"
        accept="application/pdf"
        multiple
        onChange={handleFileInput}
        className="hidden"
        id="pdf-upload"
        disabled={disabled}
      />
      <label htmlFor="pdf-upload" className="cursor-pointer block">
        <Upload className="w-10 h-10 mx-auto mb-3 text-gray-400" />
        <p className="text-gray-700 font-medium">
          Drop PDF files here or click to upload
        </p>
        <p className="text-gray-500 text-sm mt-1">Maximum file size: 100 MB</p>
      </label>
    </div>
  );
};
