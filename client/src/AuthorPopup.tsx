import React from 'react';
import { Popup } from 'semantic-ui-react';
import { Solution } from './CompetitionsTable';
import { KAGGLE_URL, AVATAR_URL } from './constants';

interface AuthorPopupProps {
  children: React.ReactNode;
  solution: Solution;
}

const AuthorPopup: React.SFC<AuthorPopupProps> = ({ children, solution }) => {
  const { authorName, authorId, avatarImage } = solution;
  const authorUrl = `${KAGGLE_URL}/${authorId}`;
  const avatarUrl = `${AVATAR_URL}/${avatarImage}`;

  const renderContent = (
    <div style={{ textAlign: 'center' }}>
      <img alt={authorName} src={avatarUrl} style={{ height: 64, width: 64 }} />
      <br />
      <a href={authorUrl}>{authorName}</a>
    </div>
  );

  return <Popup trigger={children} content={renderContent} position="left center" hoverable />;
};

export default AuthorPopup;
