import { createUseStyles } from 'react-jss'

const textColor = '#33f'
const disabledTextColor = '#999'
const hoverTextColor = '#00f'

export default createUseStyles({
    component: (disabled?: Boolean) => ({
        display: 'inline-flex',
        padding: '4px 0',
        color: disabled ? disabledTextColor : textColor,
        '&:hover, &:active': {
            color: disabled ? disabledTextColor : hoverTextColor,
        },
        pointerEvents: disabled ? 'none' : 'auto'
    })
})
