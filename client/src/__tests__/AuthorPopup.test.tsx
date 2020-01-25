import React from 'react';
import { shallow } from 'enzyme';
import { Popup } from 'semantic-ui-react';

import AuthorPopup from '../AuthorPopup';

describe('AuthorPopup', () => {
  const minimalProps = {
    title: 'test',
    discussionId: 1,
    authorName: 'test',
    authorId: 'test',
    avatarImage: '1234-kg.png',
  };

  it('renders one <Popup /> component', () => {
    const wrapper = shallow(<AuthorPopup solution={minimalProps} children={<div>test</div>} />);
    expect(wrapper.find(Popup)).toHaveLength(1);
  });
});
