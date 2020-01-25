import React from 'react';
import { Header as SemHeader, Menu } from 'semantic-ui-react';
import StarCounter from './StarCounter';
import { REPO_NAME, REPO_URL, KAGGLE_BLUE, KAGGLE_GRAY } from './constants';

const Header: React.SFC = () => (
  <Menu borderless inverted fixed="top" size="massive" style={{ backgroundColor: KAGGLE_GRAY }}>
    {/* Render as an anchor tag to enable highlighting on hover. */}
    <Menu.Item as="a">
      <SemHeader>
        <a href={`/${REPO_NAME}`} style={{ color: KAGGLE_BLUE, fontWeight: 'bold' }}>
          Kaggle Solutions
        </a>
      </SemHeader>
    </Menu.Item>
    <Menu.Item position="right" as="a">
      <StarCounter url={REPO_URL} />
    </Menu.Item>
  </Menu>
);

export default Header;
