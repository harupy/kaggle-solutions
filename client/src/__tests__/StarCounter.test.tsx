import React from 'react';
import { shallow } from 'enzyme';

import StarCounter from '../StarCounter';
import { REPO_URL } from '../constants';

describe('StarCounter', () => {
  it('renders without crashing', () => {
    const wrapper = shallow(<StarCounter url={REPO_URL} />);
    expect(wrapper).toHaveLength(1);
  });

  // TODO: Try this test when the issue below is fixed.
  // https://github.com/airbnb/enzyme/issues/2086
  // it('should fetch data on mount', () => {
  //   const wrapper = mount(<StarCounter url={REPO_URL} />);
  //   expect(wrapper.find('span').text()).toMatch(/\d+/);
  // });
});
