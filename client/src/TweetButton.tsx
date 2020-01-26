import React from 'react';
import { Icon } from 'semantic-ui-react';

interface TweetButtonProps {
  url: string;
}

const TweetButton: React.SFC<TweetButtonProps> = ({ url }) => {
  // Insert a carriage return to make it easier for users to add comments.
  const encoded = encodeURI(`\r\n${url}`);
  return (
    <a href={`https://twitter.com/intent/tweet?text=${encoded}`}>
      <Icon name="twitter" size="large" />
    </a>
  );
};

export default TweetButton;
