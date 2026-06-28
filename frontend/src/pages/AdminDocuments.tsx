import { Navigate } from 'react-router-dom';

import Page from 'pages/Page';

import { useAuth } from '@chainlit/react-client';

const AdminDocuments = () => {
  const { user } = useAuth();
  const role = user?.metadata?.role;

  if (role !== 'admin') {
    return <Navigate to="/" replace />;
  }

  return (
    <Page>
      <div
        className="flex flex-col items-center justify-center flex-grow"
        style={{ height: '100%' }}
      >
        <h1 className="text-primary text-2xl font-bold">
          Administrator: Document Management
        </h1>
        <p className="text-muted-foreground">
          This is where you will upload your RAG documentation.
        </p>
      </div>
    </Page>
  );
};

export default AdminDocuments;
