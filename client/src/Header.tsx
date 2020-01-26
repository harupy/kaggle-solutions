import React from 'react';
import { Header as SemHeader, Menu } from 'semantic-ui-react';
import TweetButton from './TweetButton';
import StarCounter from './StarCounter';
import { REPO_NAME, REPO_URL, GH_PAGES_URL, KAGGLE_BLUE, KAGGLE_GRAY } from './constants';

const Header: React.SFC = () => {
  const iconStyle = {
    padding: 10,
  };

  return (
    <Menu borderless inverted fixed="top" size="massive" style={{ backgroundColor: KAGGLE_GRAY }}>
      {/* Render as an anchor tag to enable highlighting on hover. */}
      <Menu.Item link>
        <SemHeader>
          <a href={`/${REPO_NAME}`} style={{ color: KAGGLE_BLUE, fontWeight: 'bold' }}>
            Kaggle Solutions
          </a>
        </SemHeader>
      </Menu.Item>
      <Menu.Item link position="right" style={iconStyle}>
        <TweetButton url={GH_PAGES_URL} />
      </Menu.Item>
      <Menu.Item link style={iconStyle}>
        <StarCounter url={REPO_URL} />
      </Menu.Item>
    </Menu>
  );
};

export default Header;
