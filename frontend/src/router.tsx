import getRouterBasename from '@/lib/router';
import { Navigate, createBrowserRouter } from 'react-router-dom';

import AdminDocuments from 'pages/AdminDocuments';
import AuthCallback from 'pages/AuthCallback';
import Element from 'pages/Element';
import Env from 'pages/Env';
import Home from 'pages/Home';
import LLMSettings from 'pages/LLMSettings';
import Login from 'pages/Login';
import Thread from 'pages/Thread';

export const router = createBrowserRouter(
  [
    {
      path: '/',
      element: <Home />
    },
    {
      path: '/admin/documents',
      element: <AdminDocuments />
    },
    {
      path: '/admin/settings/llm',
      element: <LLMSettings />
    },
    {
      path: '/env',
      element: <Env />
    },
    {
      path: '/thread/:id?',
      element: <Thread />
    },
    {
      path: '/element/:id',
      element: <Element />
    },
    {
      path: '/login',
      element: <Login />
    },
    {
      path: '/login/callback',
      element: <AuthCallback />
    },
    {
      path: '/share/:id',
      element: <Thread />
    },
    {
      path: '*',
      element: <Navigate replace to="/" />
    }
  ],
  { basename: getRouterBasename() }
);
