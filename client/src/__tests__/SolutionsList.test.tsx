import React from 'react';
import { shallow } from 'enzyme';

import SolutionsList from '../SolutionsList';

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
