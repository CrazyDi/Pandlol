import { OPEN_FORM, CLOSE_FORM } from 'app/actions/forms';

const initialState = {};

export default function(state = initialState, action) {
    const newState = {...state};

    switch (action.type) {
        case OPEN_FORM:
            newState[action.formName] = true;
            break;

        case CLOSE_FORM:
            newState[action.formName] = false;
            break;

        default:
            break;
    }

    return newState;
}
