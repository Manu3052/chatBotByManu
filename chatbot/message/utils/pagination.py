from django.core.paginator import Paginator as DjangoPaginator

class PaginatorConfig:

    def paging_data(self, data: any,  page_number: int = 1, page_size: int = 10):
        """
        Paginates the provided data into pages of a specified number of items.

        Parameters:
            data (any): The data to be paginated. This can be a list, queryset, or any iterable object.
            page_number (int, optional): The current page number. Defaults to 1.
            page_size (int, optional): The number of items per page. Defaults to 10.

        Returns:
            paginator (Paginator): A Paginator object that contains pagination information,
            including pages, items per page, and the total number of pages.

        Exceptions:
            None. The function assumes the provided data is an iterable object (such as a list or queryset).
        
        Example usage:
            data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            paginator = paginator_tool(data, page_number=3)
            
            # To access paginated pages:
            first_page = paginator.page(1)  # Retrieves the first page
            second_page = paginator.page(2)  # Retrieves the second page
        """
        paginator = DjangoPaginator(data, page_size) 
        try:
            page = paginator.page(page_number) 
        except Exception as e:
            return {'error': str(e)}
        
        return {
            'results': list(page),  
            'count': paginator.count,  
            'num_pages': paginator.num_pages, 
            'current_page': page_number,  
            'next': page.has_next(),  
            'previous': page.has_previous(),  
        }