import React, { useState } from 'react'
import clsx from 'clsx'

import useStyles from './styles'

interface Props {
    className?: string
    disabled?: boolean
    checkedValue?: string
    children?: React.ReactNode
}

export interface IRadioButtonsContext {
    disabled?: boolean
    checkedValue?: string
    onCheckedValueChanged: (checkedValue: string) => void
}

const radioButtonsContext: IRadioButtonsContext = {
    disabled: false,
    checkedValue: undefined,
    onCheckedValueChanged: () => {}
}

export const RadioButtonsContext = React.createContext(radioButtonsContext)

const RadioButtons = (props: Props) => {
    const [checkedValue, setCheckedValue] = useState<string|undefined>(props.checkedValue)

    const classes = useStyles({
    })

    const className = clsx(classes.component, props.className)
    const attributes: { [index: string]: any } = {}

    const radioButtonsContextProviderValue: IRadioButtonsContext = {
        disabled: props.disabled,
        checkedValue: checkedValue,
        onCheckedValueChanged: (checkedValue) => {
            setCheckedValue(checkedValue)
        }
    }

    return (
        <div
            {...attributes}
            className={className}
        >
            <RadioButtonsContext.Provider value={radioButtonsContextProviderValue}>
                {props.children}
            </RadioButtonsContext.Provider>
        </div>
    )
}

export default RadioButtons
