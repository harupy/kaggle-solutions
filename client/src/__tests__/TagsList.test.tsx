import React from 'react';
import { shallow } from 'enzyme';

import TagsList from '../TagsList';

describe('TagsList', () => {
  const categories = [{ name: 'a', tagUrl: 'tags/a' }];

  it('renders without crashing', () => {
    const wrapper = shallow(<TagsList categories={categories} />);
    expect(wrapper).toHaveLength(1);
  });
});
