import { createUseStyles } from 'react-jss'

export interface StyleProps {
    checked?: boolean
    disabled?: boolean
}

export default createUseStyles({
    component: (props: StyleProps) => ({
        display: 'inline-flex',
        alignItems: 'center',
        lineHeight: '20px',
        border: 'none',
        backgroundColor: 'initial',
        margin: '4px',
        padding: '0px',
        cursor: props.disabled ? 'default' : 'pointer',
        pointerEvents: props.disabled ? 'none' : 'inherit'
    }),
    input: (props: StyleProps) => ({
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        width: '22px',
        height: '22px',
        backgroundColor: props.disabled ? '#eee' : '#fff',
        border: '1px solid #ccc',
        marginRight: '4px'
    }),
    icon: (props: StyleProps) => ({
        display: props.checked ? 'block' : 'none'
    }),
    text: (props: StyleProps) => ({
        color: props.disabled ? '#999' : '#333'
    })
})