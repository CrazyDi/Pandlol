import { createUseStyles } from 'react-jss'

const textColor = '#333'
const backgroundColor = '#eee'
const borderColor = '#ccc'
const borderShadowColor = '#fff'
const disabledTextColor = '#999'
const disabledBackgroundColor = '#eee'
const disabledShadowColor = '#eee'
const hoverTextColor = '#000'
const hoverBackgroundColor = '#f0f0f0'

export default createUseStyles({
    component: (disabled?: Boolean) => ({
        display: 'inline-flex',
        padding: '7px 11px',
        color: disabled ? disabledTextColor : textColor,
        backgroundColor: backgroundColor,
        border: `1px solid ${borderColor}`,
        borderRadius: '2px',
        boxShadow: `1px 1px 1px 0 ${disabled ? disabledShadowColor : borderShadowColor} inset`,
        '&:hover, &:active': {
            color: disabled ? disabledTextColor : hoverTextColor,
            backgroundColor: disabled? disabledBackgroundColor: hoverBackgroundColor
        },
        cursor: disabled ? 'default' : 'pointer',
        pointerEvents: disabled ? 'none' : 'auto'
    })
})
