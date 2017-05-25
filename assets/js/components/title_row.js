import React from 'react';
import { Link } from 'react-router-dom';


// eslint-disable-next-line react/prefer-stateless-function
class TitleRow extends React.Component {

  render() {
    const btnClass = `btn btn-${this.props.btn_class}  pull-right`;

    return (
      <div className="row">
        <div className="col-sm-6">
          <h3>{this.props.title}</h3>
        </div>

        <div className="col-sm-6">
          <Link className={btnClass} to={this.props.url}>
            {this.props.btn_text}
          </Link>
        </div>
      </div>
    );
  }
}

export default TitleRow;
