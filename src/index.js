import React from 'react';
import ReactDOM from 'react-dom/client';
import { createBrowserRouter, RouterProvider } from 'react-router-dom';

import './index.css';
import Home from './Home';
import ErrorPage from './ErrorPage';
import TestPage from './TestPage';

const router = createBrowserRouter([
  {
      path: "/",
      element: <Home />,
      errorElement: <ErrorPage />
  },
  {
    path: "/test",
    element: <TestPage />,
    errorElement: <ErrorPage />
  }
]);

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);
