import React from 'react'
import Button from 'controls/Button'
import IChampionListFilter from 'app/interfaces/IChampionListFilter'
import useStyles from './styles'

interface Props {
    onSearch: (filter: IChampionListFilter) => void
}

const HomePageSearchFilter = (props: Props) => {
    const classes = useStyles()

    const handleSearch = () => {
        const filter: IChampionListFilter = {
        }

        props.onSearch(filter)
    }

    return (
        <div className={classes.root}>
            <div>
                <Button>Expand</Button>
            </div>
            <div>
                <Button onClick={handleSearch}>
                    Search
                </Button>
            </div>
        </div>
    )
}

export default HomePageSearchFilter
