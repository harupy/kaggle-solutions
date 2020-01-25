import React from 'react';
import { shallow, mount } from 'enzyme';
import { List } from 'semantic-ui-react';

import SolutionsList from '../SolutionsList';
import AuthorPopup from '../AuthorPopup';

describe('SolutionsList', () => {
  const competitionUrl = 'https://www.kaggle.com/c/titanic';
  const solutions = [
    {
      title: 'test',
      discussionId: 1,
      authorName: 'test',
      authorId: 'test',
      avatarImage: '1234-kg.png',
    },
  ];

  it('renders without crashing', () => {
    const wrapper = shallow(
      <SolutionsList solutions={solutions} competitionUrl={competitionUrl} />
    );
    expect(wrapper).toHaveLength(1);
  });
});
