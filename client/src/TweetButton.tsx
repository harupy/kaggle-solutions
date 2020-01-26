import React from 'react';
import { Icon } from 'semantic-ui-react';

interface TweetButtonProps {
  url: string;
}

const TweetButton: React.SFC<TweetButtonProps> = ({ url }) => {
  return (
    <a href={`https://twitter.com/intent/tweet?text=${url}`}>
      <Icon name="twitter" size="large" />
    </a>
  );
};

export default TweetButton;
