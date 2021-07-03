import { createUseStyles } from 'react-jss'

export interface StyleProps {
    disabled?: boolean
}

export default createUseStyles({
    component: (props: StyleProps) => ({
        display: 'inline-flex',
        lineHeight: '20px',
        margin: '4px',
        color: props.disabled ? '#999' : '#333'
    })
})
