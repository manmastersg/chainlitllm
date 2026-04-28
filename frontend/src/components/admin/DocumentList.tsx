import { Eye, Trash2 } from 'lucide-react';

export interface Document {
  doc_id: string;
  filename: string;
  status: 'pending' | 'indexing' | 'ready' | 'failed';
  page_count: number;
  added_at: number;
  progress?: number;
  current_page?: number;
}

interface DocumentListProps {
  documents: Document[];
  onView: (doc: Document) => void;
  onDelete: (doc: Document) => void;
}

export const DocumentList = ({
  documents,
  onView,
  onDelete
}: DocumentListProps) => {
  if (documents.length === 0) {
    return (
      <div className="text-center py-12 text-gray-500">
        <p>No documents uploaded yet.</p>
        <p className="text-sm mt-1">Upload your first PDF above.</p>
      </div>
    );
  }

  const getStatusBadge = (doc: Document) => {
    switch (doc.status) {
      case 'ready':
        return <span className="text-green-600 font-medium">✅ Ready</span>;
      case 'indexing':
        return <span className="text-amber-600 font-medium">⏳ Indexing</span>;
      case 'failed':
        return <span className="text-red-600 font-medium">❌ Failed</span>;
      default:
        return <span className="text-gray-500">⏳ Pending</span>;
    }
  };

  return (
    <div className="space-y-3 mt-6">
      {documents.map((doc) => (
        <div
          key={doc.doc_id}
          className={`
            p-4 rounded-lg border transition-all
            ${doc.status === 'indexing' ? 'border-amber-300 bg-amber-50' : 'border-gray-200 bg-white'}
          `}
        >
          <div className="flex items-center justify-between">
            <div className="flex-1">
              <p className="font-medium text-gray-900">{doc.filename}</p>
              <p className="text-sm text-gray-500 mt-0.5">
                {doc.page_count > 0 ? `${doc.page_count} pages` : ''}
              </p>
            </div>

            <div className="flex items-center gap-4">
              {doc.status === 'indexing' && doc.progress !== undefined && (
                <div className="w-32">
                  <div className="w-full h-2 bg-gray-200 rounded-full overflow-hidden">
                    <div
                      className="h-full bg-amber-500 transition-all duration-300"
                      style={{ width: `${doc.progress}%` }}
                    />
                  </div>
                  <p className="text-xs text-gray-500 mt-1 text-right">
                    {doc.progress}%
                  </p>
                </div>
              )}

              {getStatusBadge(doc)}

              <div className="flex gap-2 ml-2">
                {doc.status === 'ready' && (
                  <button
                    onClick={() => onView(doc)}
                    className="p-1.5 text-gray-500 hover:text-gray-700 hover:bg-gray-100 rounded"
                  >
                    <Eye size={18} />
                  </button>
                )}
                <button
                  onClick={() => onDelete(doc)}
                  className="p-1.5 text-gray-500 hover:text-red-600 hover:bg-red-50 rounded"
                >
                  <Trash2 size={18} />
                </button>
              </div>
            </div>
          </div>
        </div>
      ))}
    </div>
  );
};
