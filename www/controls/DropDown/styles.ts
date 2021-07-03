import { createUseStyles } from 'react-jss'

export interface StyleProps {
    disabled?: boolean
    editable?: boolean
}

export default createUseStyles({
    component: (props: StyleProps) => ({
        display: 'inline-flex',
        margin: '4px'
    }),
    content: (props: StyleProps) => ({
        position: 'relative',
        flex: 'auto'
    }),
    inputContent: (props: StyleProps) => ({
        display: 'flex',
        backgroundColor: '#eee',
        zIndex: 7,
        border: '1px solid #ccc'
    }),
    input: (props: StyleProps) => ({
        position: 'relative',
        lineHeight: '18px',
        padding: '6px 10px',
        width: '100%',
        color: props.disabled ? '#999' : '#333',
        borderWidth: props.editable ? '0 1px 0 0' : '0',
        borderStyle: 'solid',
        borderColor: '#ccc',
        marginRight: props.editable ? '1px' : 'inherit',
        backgroundColor: props.editable ? '#fff' : 'transparent',
        pointerEvents: props.disabled ? 'none' : 'inherit'
    }),
    input_Readonly: {
        cursor: 'default'
    },
    inputArrow: (props: StyleProps) => ({
        minWidth: '32px',
        border: 'none',
        boxShadow: props.editable ? '1px 1px 3px -1px #fff inset' : 'none',
        cursor: 'pointer',
        display: 'inline-flex',
        alignItems: 'center',
        justifyContent: 'center',
        padding: '0',
        backgroundColor: '#eee',
        pointerEvents: props.disabled ? 'none' : 'inherit'
    }),
    inputButton: (props: StyleProps) => ({
        position: 'absolute',
        top: '0px',
        left: '0px',
        width: '100%',
        height: '100%',
        border: '1px solid transparent',
        backgroundColor: 'transparent',
        cursor: 'pointer',
        pointerEvents: props.disabled ? 'none' : 'inherit'
    }),
    list: {
        boxSizing: 'border-box',
        position: 'absolute',
        zIndex: 8,
        width: '100%',
        border: '1px solid #ccc',
        borderTop: '1px solid transparent',
        display: 'flex',
        flexDirection: 'column'
    },
    listItemsEmpty: {
        padding: '6px 10px',
        color: '#999',
        backgroundColor: '#fcfcfc'
    },
    listItem: {
        display: 'inline-flex',
        padding: '6px 10px',
        border: '1px solid #fff',
        backgroundColor: '#fff',
        color: '#333',
        cursor: 'pointer',
        '&:hover, &:active': {
            color: '#000'
        }
    },
    listItem_Disabled: {
        color: '#999',
        '&:hover, &:active': {
            color: '#999'
        },
        cursor: 'default'
    },
    listItem_Selected: {
        backgroundColor: '#eee',
        border: '1px solid #eee'
    }
})
