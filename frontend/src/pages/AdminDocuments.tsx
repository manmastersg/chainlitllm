import { Navigate } from 'react-router-dom';

import { useAuth } from '@chainlit/react-client';

const AdminDocuments = () => {
  const { user } = useAuth();
  const role = user?.metadata?.role;

  if (role !== 'admin') {
    return <Navigate to="/" replace />;
  }

  return (
    <div
      style={{
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
        height: '100vh',
        width: '100vw',
        backgroundColor: 'var(--background)'
      }}
    >
      <h1 style={{ color: 'var(--primary)', fontSize: '2rem' }}>
        Administrator: Document Management
      </h1>
      <p style={{ color: 'var(--muted-foreground)' }}>
        This is where you will upload your RAG documentation.
      </p>
    </div>
  );
};

export default AdminDocuments;
