import { createUseStyles } from 'react-jss'

export default createUseStyles({
    component: {
        position: 'relative',
        display: 'inline-flex',
        alignItems: 'center',
        justifyContent: 'center',
        width: '24px',
        height: '24px'
    },
    content: {
        position: 'absolute',
        width: '16px',
        height: '16px',
        borderRadius: '50%',
        borderStyle: 'solid',
        borderWidth: '2px',
        borderColor: '#36b transparent #36b transparent',
        animation: 'preloader-dual-ring 1.2s linear infinite'
    }
})