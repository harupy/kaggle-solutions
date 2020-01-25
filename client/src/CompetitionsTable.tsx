import React, { useState } from 'react';
import data from './competitions.json';
import { Table, Input, Message } from 'semantic-ui-react';

import SolutionsList from './SolutionsList';
import TagsList from './TagsList';
import { formatDate, isDateKey, basename, isDateOver } from './utils';

export interface Solution {
  title: string;
  discussionId: number;
  authorName: string;
  authorId: string;
  avatarImage: string;
}

interface Competition {
  [key: string]: any;
  competitionTitle: string;
  competitionUrl: string;
  competitionId: number;
  thumbnailImageUrl: string;
  rewardDisplay: string;
  evaluationMetric: string;
  enabledDate: string;
  deadline: string;
  totalTeams: number;
  categories: {
    categories: { tagUrl: string }[];
  };
  solutions?: Solution[];
}

const CompetitionsTable: React.FC = () => {
  const competitions: Competition[] = [...data];
  const [searchTerm, setSearchTerm] = useState<string>('');

  const mapper: { [key: string]: string } = {
    rewardDisplay: 'Reward [USD]',
    evaluationMetric: 'Metric',
    enabledDate: 'Start',
    deadline: 'End',
    totalTeams: '# of Teams',
  };

  const handleChange = (event: React.ChangeEvent<HTMLInputElement>): void => {
    event.preventDefault();
    setSearchTerm(event.target.value);
  };

  const search = (): Competition[] =>
    competitions.filter(comp => {
      return comp.competitionTitle.toLowerCase().includes(searchTerm.toLowerCase());
    });

  return (
    <div>
      <Input label="Search Competition" onChange={handleChange} />
      <Message compact positive size="mini" style={{ marginLeft: 10 }}>
        Colored competitions are ongoing.
      </Message>
      <Table celled>
        <Table.Header>
          <Table.Row>
            {['Logo', 'Title', 'Tags', 'Solutions', ...Object.values(mapper)].map((val, idx) => (
              <Table.HeaderCell textAlign={idx === 0 ? 'center' : undefined} key={val}>
                {val}
              </Table.HeaderCell>
            ))}
          </Table.Row>
        </Table.Header>

        <Table.Body>
          {search().map(comp => (
            <Table.Row key={comp.competitionId} positive={!isDateOver(comp.deadline)}>
              {/* competition logo */}
              <Table.Cell textAlign="center">
                <img src={comp.thumbnailImageUrl} alt="" style={{ height: 100 }} />
              </Table.Cell>
              {/* competition link */}
              <Table.Cell>
                {/* Note that `competitionUrl` starts with "/" */}
                <a
                  href={`https://kaggle.com${comp.competitionUrl}`}
                  target="_blank"
                  rel="noopener noreferrer"
                >
                  {comp.competitionTitle}
                </a>
              </Table.Cell>
              <Table.Cell>
                <TagsList tags={comp.categories.categories.map(({ tagUrl }) => basename(tagUrl))} />
              </Table.Cell>
              <Table.Cell style={{ width: 200 }}>
                <SolutionsList
                  competitionUrl={comp.competitionUrl}
                  solutions={comp.solutions ? comp.solutions : []}
                />
              </Table.Cell>
              {Object.keys(mapper).map(key => (
                <Table.Cell key={key}>
                  {isDateKey(key) ? formatDate(comp[key]) : comp[key]}
                </Table.Cell>
              ))}
            </Table.Row>
          ))}
        </Table.Body>
      </Table>
    </div>
  );
};

export default CompetitionsTable;
