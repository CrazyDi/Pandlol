import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';

import { closeForm } from 'app/actions/forms';

import Form from './component';

const mapStateToProps = (state) => {
    return {
        forms: state.forms
    }
};

const mapDispatchToProps = (dispatch) => {
    return {
        closeForm: bindActionCreators(closeForm, dispatch)
    };
};

export default connect(mapStateToProps, mapDispatchToProps)(Form);
