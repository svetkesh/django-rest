import React, { Component } from 'react';

class App extends Component {
  state = {
    menu: []
  };

  async componentDidMount() {
    try {
      const res = await fetch('http://127.0.0.1:8000/api/');
      const menu = await res.json();
      console.log(menu);
      this.setState({
        menu
      });
    } catch (e) {
      console.log(e);
    }
  }

  render() {
    return (
      <div  className="customers--list">
          <table  className="table">
          <thead  key="thead">
          <tr>
              <th>#</th>
              <th>title</th>
              <th>description</th>
              <th>cost</th>
          </tr>
          </thead>
          <tbody>
          {this.state.menu.map( menu  =>
              <tr  key={menu.id}>
              <td>{menu.id}  </td>
              <td>{menu.title}</td>
              <td>{menu.description}</td>
              <td>{menu.cost}</td>
          </tr>)}
          </tbody>
          </table>
      </div>
    );
  }
}

export default App;
