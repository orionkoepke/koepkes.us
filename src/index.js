import React from 'react';
import ReactDOM from 'react-dom/client';
import { createBrowserRouter, RouterProvider } from 'react-router-dom';

import './index.css';
import Home from './Home';
import ErrorPage from './ErrorPage';
import OrionResume from './OrionResume/OrionResume';


function getSubdomain(){
  return window.location.host.split(".")[0];
}

function getUrlWithSubdomainAsPath(){
  var location = window.location;
  var subdomain = getSubdomain();
  var newHostName = location.host.replace(`${subdomain}.`, '', 1);
  return `${location.protocol}//${newHostName}/${subdomain}`;
}

function goToUrl(url){
  console.log(`Redirecting from ${window.location.href} to ${url}`);
  window.location.replace(url);
}

function render(){
  const router = createBrowserRouter([
    {
        path: "/",
        element: <Home />,
        errorElement: <ErrorPage />
    },
    {
      path: "/orion",
      element: <OrionResume />,
      errorElement: <ErrorPage />
    }
  ]);

  const root = ReactDOM.createRoot(document.getElementById('root'));
  root.render(
    <React.StrictMode>
      <RouterProvider router={router} />
    </React.StrictMode>
  );
}


switch(getSubdomain().toLowerCase()){
  case "orion":
    goToUrl(getUrlWithSubdomainAsPath());
    break;
  default:
    render();
}
