import { connect } from 'react-redux';

import InfoForm from './component';

const mapStateToProps = (state) => {
    return {
        pipe: state.pipes.selectedPipe
    };
};

export default connect(mapStateToProps, null)(InfoForm);
