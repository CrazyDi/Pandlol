import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';

import { openForm } from 'app/actions/forms';

import Header from './component';

const mapStateToProps = (state) => {
    return {
    };
};

const mapDispatchToProps = (dispatch) => {
    return {
        openForm: bindActionCreators(openForm, dispatch),
    };
};

export default connect(mapStateToProps, mapDispatchToProps)(Header);
