import { createUseStyles } from 'react-jss'

export interface StyleProps {
    checked: boolean
    disabled?: boolean
}

export default createUseStyles({
    component: (props: StyleProps) => ({
        display: 'inline-flex',
        alignItems: 'center',
        border: 'none',
        backgroundColor: 'initial',
        margin: '4px',
        padding: '0px',
        color: props.disabled ? '#999' : '#333',
        cursor: props.disabled ? 'default' : 'pointer',
        pointerEvents: props.disabled ? 'none' : 'inherit'
    }),
    input: (props: StyleProps) => ({
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        width: '22px',
        height: '22px',
        borderRadius: '50%',
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
