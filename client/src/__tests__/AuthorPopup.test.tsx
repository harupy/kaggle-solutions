import React from 'react';
import { shallow } from 'enzyme';
import { Popup } from 'semantic-ui-react';

import AuthorPopup from '../AuthorPopup';

describe('AuthorPopup', () => {
  const solution = {
    title: 'test',
    discussionId: 1,
    authorName: 'test',
    authorId: 'test',
    avatarImage: '1234-kg.png',
  };

  it('renders without crashing', () => {
    const wrapper = shallow(<AuthorPopup solution={solution} children={<div>test</div>} />);
    expect(wrapper.find(Popup)).toHaveLength(1);
  });
});
