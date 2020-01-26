import React, { useState, useEffect } from 'react';
import { Icon } from 'semantic-ui-react';

interface StarCounterProps {
  url: string;
}

const StarCounter: React.FC<StarCounterProps> = ({ url }) => {
  const [starCount, setStarCount] = useState<number | undefined>();

  // Fetch stargazers count GitHub using the GitHub REST API.
  const fetchStarCount = async () => {
    const [user, repo] = url
      .split('/')
      .slice(1)
      .slice(-2);
    const API_URL = `https://api.github.com/repos/${user}/${repo}`;
    const resp = await fetch(API_URL);
    console.log(resp);

    if (!resp.ok) {
      throw new Error(`${resp.status} ${resp.statusText}`);
    }

    const data = await resp.json();
    setStarCount(data.stargazers_count);
  };

  useEffect(() => {
    fetchStarCount();
  }, []);

  if (starCount === undefined) {
    return null;
  }

  const valign = { verticalAlign: 'middle' };

  return (
    <a href={url}>
      <Icon name="github" size="large" style={valign} />
      <span style={{ verticalAlign: 'middle' }}>{starCount}</span>
      <Icon name="star" size="small" style={{ marginLeft: 5 }} />
    </a>
  );
};

export default StarCounter;
