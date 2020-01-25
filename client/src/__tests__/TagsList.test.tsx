import React from 'react';
import { shallow, mount } from 'enzyme';
import { Label } from 'semantic-ui-react';

import TagsList from '../TagsList';

describe('TagsList', () => {
  const minimalProps = [{ name: 'a', tagUrl: 'tags/a' }];

  it('renders one <Label.Group /> component', () => {
    const wrapper = shallow(<TagsList categories={minimalProps} />);
    expect(wrapper.find(Label.Group)).toHaveLength(1);
  });

  it('renders one <Label /> component', () => {
    const wrapper = shallow(<TagsList categories={minimalProps} />);
    expect(wrapper.find(Label)).toHaveLength(1);
  });

  it('renders a div which contains "a"', () => {
    const wrapper = mount(<TagsList categories={minimalProps} />);
    expect(wrapper.find('div.ui.label').text()).toEqual('a');
  });
});
