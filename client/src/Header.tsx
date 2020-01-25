import React from 'react';
import { Menu } from 'semantic-ui-react';
import { KAGGLE_BLUE, KAGGLE_GRAY } from './constants';

const Header: React.SFC = () => (
  <Menu borderless inverted fixed="top" size="massive" style={{ backgroundColor: KAGGLE_GRAY }}>
    <Menu.Item style={{ color: KAGGLE_BLUE, fontWeight: 'bold' }}>Kaggle Solutions</Menu.Item>
  </Menu>
);

export default Header;
