import React from 'react';
import { Container } from 'semantic-ui-react';
import CompetitionsTable from './CompetitionsTable';
import Header from './Header';

const App: React.FC = () => (
  <div>
    <Header />
    <Container fluid style={{ paddingTop: 80, paddingLeft: 10, paddingRight: 10 }}>
      <CompetitionsTable />
    </Container>
  </div>
);

export default App;
