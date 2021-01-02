import { createUseStyles } from 'react-jss'

const textColor = '#00f'
const disabledTextColor = '#999'
const hoverTextColor = '#55f'

export default createUseStyles({
    component: (disabled?: Boolean) => ({
        display: 'inline-flex',
        padding: '4px 0',
        color: disabled ? disabledTextColor : textColor,
        '&:hover': {
            color: disabled ? disabledTextColor : hoverTextColor,
        },
        pointerEvents: disabled ? 'none' : 'auto'
    })
})
