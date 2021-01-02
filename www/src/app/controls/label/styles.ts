import { createUseStyles } from 'react-jss'

const textColor = '#333'
const disabledTextColor = '#999'

export default createUseStyles({
    component: (disabled?: Boolean) => ({
        display: 'inline-flex',
        padding: '4px 0',
        color: disabled ? disabledTextColor : textColor
    })
})
