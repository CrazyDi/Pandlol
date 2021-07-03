import { createUseStyles } from 'react-jss'

export interface StyleProps {
    disabled?: boolean
}

export default createUseStyles({
    component: (props: StyleProps) => ({
        lineHeight: '20px',
        margin: '4px',
        padding: '5px 11px',
        border: '1px solid #ccc',
        color: props.disabled ? '#999' : '#333',
        backgroundColor: props.disabled ? '#eee': '#fff',
        pointerEvents: props.disabled ? 'none' : 'inherit'
    }),
    input: (props: StyleProps) => ({
    }),
    textarea: (props: StyleProps) => ({
        resize: 'none'
    })
})
