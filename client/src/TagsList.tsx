import React from 'react';
import { Label } from 'semantic-ui-react';

interface TagsListProps {
  tags: (string | undefined)[];
}

const TagsList: React.SFC<TagsListProps> = ({ tags }) => {
  return <Label.Group>{tags.map(tag => tag && <Label key={tag}>{tag}</Label>)}</Label.Group>;
};

export default TagsList;
