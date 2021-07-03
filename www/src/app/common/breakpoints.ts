export enum BreakPoint {
    SS_320,
    XS_480,
    SM_640,
    SX_800,
    MD_960,
    LG_1200,
    XL_1600
}

const getBreakPointWidth = (breakPoint: BreakPoint): number => {
    switch (breakPoint) {
        case BreakPoint.SS_320:
            return 320
        case BreakPoint.XS_480:
            return 480
        case BreakPoint.SM_640:
            return 640
        case BreakPoint.SX_800:
            return 800
        case BreakPoint.MD_960:
            return 960
        case BreakPoint.LG_1200:
            return 1200
        case BreakPoint.XL_1600:
            return 1600
        default:
            return 0
    }

}

const getMedia = (minWidth: BreakPoint, maxWidth: number) => {
    const values = ['@media only screen']

    if (minWidth) {
        values.push(`and (min-width: ${minWidth}px)`)
    }

    if (maxWidth) {
        values.push(`and (max-width: ${maxWidth - 1}px)`)
    }

    return values.join(' ')
}

export default {
    equalOrDown: (breakPoint: BreakPoint) => {
        const maxWidth = getBreakPointWidth(breakPoint + 1)

        return getMedia(0, maxWidth)
    },
    equalOrUp: (breakPoint: BreakPoint) => {
        const minWidth = getBreakPointWidth(breakPoint)

        return getMedia(minWidth, 0)
    }
}
