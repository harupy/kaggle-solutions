import React from 'react';
import { List } from 'semantic-ui-react';
import AuthorPopup from './AuthorPopup';
import { KAGGLE_URL } from './constants';
import { Solution } from './CompetitionsTable';

interface SolutionsListProps {
  competitionUrl: string;
  solutions: Solution[];
}

const SolutionsList: React.SFC<SolutionsListProps> = ({ competitionUrl, solutions }) => {
  return (
    <List>
      {solutions.map(sol => (
        <AuthorPopup key={`${competitionUrl}-${sol.discussionId}`} solution={sol}>
          <List.Item>
            <a href={`${KAGGLE_URL}${competitionUrl}/discussion/${sol.discussionId}`}>
              {sol.title}
            </a>
          </List.Item>
        </AuthorPopup>
      ))}
    </List>
  );
};

export default SolutionsList;
