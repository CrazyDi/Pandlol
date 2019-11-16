export const OPEN_FORM = 'OPEN_FORM';
export const CLOSE_FORM = 'CLOSE_FORM';

export function openForm(formName) {
    return {
        type: OPEN_FORM,
        formName
    };
}

export function closeForm(formName) {
    return {
        type: CLOSE_FORM,
        formName
    };
}
