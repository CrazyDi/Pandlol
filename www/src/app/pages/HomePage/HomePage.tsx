import React from 'react'
import Label from 'controls/Label'
import MasterPage from 'app/components/MasterPage'
import ISearchResultItem from 'app/interfaces/ISearchResultItem'
import HomePageSearchFilter from './SearchFilter'
import HomePageSearchResult from './SearchResult'
import useStyles from './styles'

interface Props {
}

const HomePage = (props: Props) => {
    const classes = useStyles()

    const searchResultItems: ISearchResultItem[] = [
    ]

    return (
        <MasterPage>
            <div className={classes.root}>
                <Label>Home Page</Label>
                <br/>

                <HomePageSearchFilter />
                <HomePageSearchResult items={searchResultItems} />
            </div>
        </MasterPage>
    )
}

export default HomePage
