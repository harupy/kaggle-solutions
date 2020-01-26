import React from 'react';
import { shallow } from 'enzyme';

import TweetButton from '../TweetButton';
import { GH_PAGES_URL } from '../constants';

describe('TweetButton', () => {
  it('renders without crashing', () => {
    const wrapper = shallow(<TweetButton url={GH_PAGES_URL} />);
    expect(wrapper).toHaveLength(1);
  });
});
