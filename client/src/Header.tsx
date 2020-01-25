import React from 'react';
import { Header as SemHeader, Menu } from 'semantic-ui-react';
import StarCounter from './StarCounter';
import { KAGGLE_BLUE, KAGGLE_GRAY } from './constants';

const Header: React.SFC = () => (
  <Menu borderless inverted fixed="top" size="massive" style={{ backgroundColor: KAGGLE_GRAY }}>
    <Menu.Item>
      <SemHeader style={{ color: KAGGLE_BLUE, fontWeight: 'bold' }}>Kaggle Solutions</SemHeader>
    </Menu.Item>
    <Menu.Item position="right" onClick={() => {}}>
      <StarCounter url="https://github.com/harupy/kaggle-solutions" />
    </Menu.Item>
  </Menu>
);

export default Header;
