import React from 'react';
import { Header as SemHeader, Menu } from 'semantic-ui-react';
import StarCounter from './StarCounter';
import { KAGGLE_BLUE, KAGGLE_GRAY } from './constants';

const Header: React.SFC = () => (
  <Menu borderless inverted fixed="top" size="massive" style={{ backgroundColor: KAGGLE_GRAY }}>
    <Menu.Item as="a">
      <SemHeader>
        <a href="/" style={{ color: KAGGLE_BLUE, fontWeight: 'bold' }}>
          Kaggle Solutions
        </a>
      </SemHeader>
    </Menu.Item>
    {/* Render as an anchor tag to enable highlighting on hover. */}
    <Menu.Item position="right" as="a">
      <StarCounter url="https://github.com/harupy/kaggle-solutions" />
    </Menu.Item>
  </Menu>
);

export default Header;
