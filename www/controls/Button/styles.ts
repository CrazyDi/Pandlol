import { createUseStyles } from 'react-jss'

export interface StyleProps {
    disabled?: boolean
}

export default createUseStyles({
    component: (props: StyleProps) => ({
        display: 'inline-flex',
        lineHeight: '20px',
        margin: '4px',
        padding: '5px 11px',
        color: props.disabled ? '#999' : '#333',
        backgroundColor: '#eee',
        border: '1px solid #ccc',
        boxShadow: `1px 1px 1px 0 ${props.disabled ? '#eee' : '#fff'} inset`,
        '&:hover, &:active': {
            color: props.disabled ? '#999' : '#000',
            backgroundColor: props.disabled ? '#eee' : '#f0f0f0'
        },
        cursor: props.disabled ? 'default' : 'pointer',
        pointerEvents: props.disabled ? 'none' : 'inherit'
    })
})
