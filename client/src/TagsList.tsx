import React from 'react';
import { Label } from 'semantic-ui-react';
import { Category } from './CompetitionsTable';

interface TagsListProps {
  categories: Category[];
}

const TagsList: React.SFC<TagsListProps> = ({ categories }) => {
  return (
    <Label.Group>
      {categories.map(({ name }) => (
        <Label key={name}>{name}</Label>
      ))}
    </Label.Group>
  );
};

export default TagsList;
